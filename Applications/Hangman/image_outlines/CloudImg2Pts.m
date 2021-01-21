clear;

cloud_img = imread('Cloud.jpg');
cloud_bw = edge(rgb2gray(cloud_img));

cloud_bw(1:75, 600:end) = false; % Take out top right thing
imshow(cloud_bw);

[y_pts, x_pts] = find(cloud_bw);

y_pts = -y_pts;

x_pts = x_pts - min(x_pts);
y_pts = y_pts - min(y_pts);


plot(x_pts, y_pts, '.k');

max_x = max(x_pts);

x_pts = x_pts./max_x;
y_pts = y_pts./max_x;

cloud_pts = [x_pts, y_pts];

cloud_pts_new = cloud_pts(1,:);
cloud_pts(1,:) = [];

[~, cloud_pts] = kmeans(cloud_pts, 120);

num_pts = 1;

while true
    current_pt = cloud_pts_new(num_pts,:);
    
    % Find closest point
    distances = sqrt((current_pt(1) - cloud_pts(:,1)).^2 + (current_pt(2) - cloud_pts(:,2)).^2);
    [dist, ind] = min(distances);
    
    % Add closest point to new pts
    if dist < 1
        new_pt = cloud_pts(ind,:);
        cloud_pts(ind,:) = [];
        num_pts = num_pts + 1;
        cloud_pts_new(num_pts,:) = new_pt;
    else
        break;
    end
    
    figure(1);
    clf;
    plot(cloud_pts_new(:,1), cloud_pts_new(:,2), '.k');
end

writematrix(cloud_pts_new, 'cloud_pts.csv', 'Delimiter', ',');

